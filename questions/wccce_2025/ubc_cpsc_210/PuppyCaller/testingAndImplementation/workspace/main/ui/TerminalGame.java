package ui;

import com.googlecode.lanterna.TerminalSize;
import com.googlecode.lanterna.TextColor;
import com.googlecode.lanterna.graphics.TextGraphics;
import com.googlecode.lanterna.input.KeyStroke;
import com.googlecode.lanterna.screen.Screen;
import com.googlecode.lanterna.terminal.DefaultTerminalFactory;
import model.*;

import java.io.IOException;
import java.util.Comparator;

// represents the terminal/ui of the game
public class TerminalGame {
    private Game game;
    private Screen screen;
    private PuppyCaller puppyCaller;

    // MODIFIES: this
    // EFFECTS:  initializes the terminal and starts the game from a given wordlist
    public void start(WordList wordList) throws IOException, InterruptedException {
        screen = new DefaultTerminalFactory()
                .setPreferTerminalEmulator(false)
                .setInitialTerminalSize(new TerminalSize(100, 40))
                .createScreen();

        screen.startScreen();
        screen.doResizeIfNecessary();
        screen.setCursorPosition(null);

        TerminalSize terminalSize = screen.getTerminalSize();

        game = new Game(
                terminalSize.getColumns() - 5,
                // first row is reserved for us
                terminalSize.getRows(),
                wordList
        );
        puppyCaller = new PuppyCaller();

        beginTicks();
    }

    // EFFECTS: runs tick Game.TICKS_PER_SECOND times per second until the game is over, then exits
    private void beginTicks() throws IOException, InterruptedException {
        while (!game.isEndedGame()) {
            tick();
            Thread.sleep(1000L / Game.TICKS_PER_SECOND);
        }

        System.exit(0);
    }

    private void tick() throws IOException {
        handleUserInput();

        game.tick();

        // todo: add level transition
        if (game.isEndedLevel()) {
            game.advanceLevel();
        }

        screen.clear();
        render();
        screen.refresh();
    }

    // EFFECTS: checks for user input, if one exists, call puppyCaller to handle the input
    private void handleUserInput() throws IOException {
        KeyStroke stroke = screen.pollInput();

        if (stroke == null || stroke.getCharacter() == null) {
            return;
        }

        char c = stroke.getCharacter();
        puppyCaller.handleInput(game.getPuppiesToCall(), c);
    }

    private void render() {
        drawString("Level " + (game.getLevelIndex() + 1), TextColor.ANSI.MAGENTA, 0, 0);
        renderFence();
        drawPlayer();
        game.getPuppies()
                .stream()
                .sorted(Comparator.comparing(p -> p.hasBeenCalled() ? 0 : 1))
                .forEach(this::drawPuppy);
    }

    private void renderFence() {
        for (int y = 1; y < game.getMaxY(); y++) {
            char character = y % 5 == 0 ? '+' : '|';

            drawCharacter(character, TextColor.ANSI.CYAN, game.getMaxX(), y);
        }
    }

    // |=|=|
    //   |
    //  | |
    private void drawPlayer() {
        TextColor c = TextColor.ANSI.GREEN;
        Player p = game.getPlayer();
        int px = p.getX();
        int py = p.getY();

        drawHead(c, px, py - 1);
        drawBody(c, px, py);
        drawLegs(c, px, py + 1);
    }

    //             (  puppy!  )
    //              /
    //             O
    // draw head |=|=|
    private void drawHead(TextColor c, int px, int py) {
        Puppy puppy = puppyCaller.getCurrentPuppy();

        if (puppy != null) {
            drawString("( ", c, px, py - 3);
            drawPuppyWord(puppy, TextColor.ANSI.MAGENTA, px + 2 + (puppy.getName().length() / 2), py - 5);
            drawString("! )", c, px + 2 + puppy.getName().length(), py - 3);

            drawCharacter('/', c, px + 1, py - 2);
        }

        drawCharacter('O', c, px, py - 1);

        drawCharacter('|', c, px - 2, py);
        drawCharacter('=', c, px - 1, py);
        drawCharacter('|', c, px, py);
        drawCharacter('=', c, px + 1, py);
        drawCharacter('|', c, px + 2, py);
    }

    private void drawBody(TextColor c, int px, int py) {
        drawCharacter('|', c, px, py);
    }

    private void drawLegs(TextColor c, int px, int py) {
        // draw feet | |
        drawCharacter('|', c, px - 1, py);
        drawCharacter('|', c, px + 1, py);
    }

    private void drawPuppy(Puppy puppy) {
        TextColor c = puppy.hasBeenCalled() ? TextColor.ANSI.BLUE : TextColor.ANSI.YELLOW;
        int ex = puppy.getX();
        int ey = puppy.getY();

        if (puppy == puppyCaller.getCurrentPuppy()) {
            c = TextColor.ANSI.MAGENTA;
        }

        drawString("     __  ", c, ex - 4, ey - 2);
        drawString("(___()'`;", c, ex - 4, ey - 1);
        drawString("/,    /` ", c, ex - 4, ey);

        if (puppy.isStriding()) {
            drawString("\\\\   \\\\", c, ex - 4, ey + 1);
        } else {
            drawString("//   //", c, ex - 5, ey + 1);
        }

        drawPuppyWord(puppy, c, ex, ey);
    }

    private void drawPuppyWord(Puppy puppy, TextColor baseColor, int ex, int ey) {
        String typed = puppy.getTypedPortion();
        String untyped = puppy.getUntypedPortion();
        int wordStart = ex - (puppy.getName().length() / 2);
        int untypedStart = wordStart + typed.length();
        TextColor typedColor = puppy.hasBeenCalled() ? baseColor : TextColor.ANSI.YELLOW;

        drawString(typed, typedColor, wordStart, ey + 2);
        drawString(untyped, baseColor, untypedStart, ey + 2);
    }

    private void drawString(String s, TextColor c, int startX, int y) {
        char[] chars = s.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            drawCharacter(chars[i], c, startX + i, y);
        }
    }

    /**
     * Draws a character in a given position on the terminal.
     */
    private void drawCharacter(char c, TextColor color, int x, int y) {
        TextGraphics text = screen.newTextGraphics();
        text.setForegroundColor(color);
        text.putString(x, y + 1, String.valueOf(c));
    }
}
