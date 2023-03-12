clear
close all

%% original plot

% set initial conditions
v0 = 40; % initial speed in m/s
theta = pi/4; % initial angle in radians

% create starter data
t = 0:0.1:15; % time in seconds

% simulate horizontal and vertical motion
x = v0 .* cos(theta) .* t;
y = v0 .* sin(theta) .* t - 9.8 .* t.^2 ./ 2; 

% plot vertical motion vs. horizontal motion
plot(x(y>=0), y(y>=0),'LineWidth',3);
grid on;
ax = gca;
ax.FontSize = 20;

print('ProjectileMotionOriginalPlot.png','-dpng');

%% plot with markers


% set initial conditions
v0 = 40; % initial speed in m/s
theta = pi/4; % initial angle in radians

% create starter data
t = 0:0.1:15; % time in seconds

% simulate horizontal and vertical motion
x = v0 .* cos(theta) .* t;
y = v0 .* sin(theta) .* t - 9.8 .* t.^2 ./ 2; 

% plot vertical motion vs. horizontal motion
plot(x(y>=0), y(y>=0),'LineWidth',3,'Marker','o');
grid on;
ax = gca;
ax.FontSize = 20;

print('ProjectileMotionWithMarkers.png','-dpng');

%% plot with better resolution


% set initial conditions
v0 = 40; % initial speed in m/s
theta = pi/4; % initial angle in radians

% create starter data
t = 0:0.005:15; % time in seconds

% simulate horizontal and vertical motion
x = v0 .* cos(theta) .* t;
y = v0 .* sin(theta) .* t - 9.8 .* t.^2 ./ 2; 

% plot vertical motion vs. horizontal motion
plot(x(y>=0), y(y>=0),'LineWidth',3,'Marker','o');
grid on;
ax = gca;
ax.FontSize = 20;

print('ProjectileMotionWithBetterResolution.png','-dpng');
