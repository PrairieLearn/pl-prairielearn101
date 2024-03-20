"""
Author: David G C. Cooper
email: dcooper@wcupa.edu
Purpose: multiple select question for Polymorphism. Many random names for classes, interfaces, and methods
"""

import random, math

import random


"""
This is the question.html for reference
    public interface {{params.interface_type}} {
        void {{params.interface_method}}();
    }
    
    public class {{params.parent_type}} {
        void {{params.parent_method}}() {
            System.out.println("{{params.parent_type}} calling {{params.parent_method}}()");
        }
    }
    
    public class {{params.child_type}} extends {{params.parent_type}} implements {{params.interface_type}} {
        void {{params.interface_method}}() {
            System.out.println("{{params.child_type}} calling {{params.interface_method}}()");
        }
    }
    
    public class Polymorphism {
        public static void main(String[] args) {
            {{params.interface_type}} {{params.interface_id}} = new {{params.child_type}}();
            {{params.parent_type}} {{params.parent_id}} = new {{params.parent_type}}();
            {{params.child_type}} {{params.child_id}} = new {{params.child_type}}();
            {{params.interface_type}} {{params.child_interface_id}} = {{params.child_id}};
            {{params.parent_type}} {{params.child_parent_id}} = {{params.child_id}};
            {{params.parent_type}} {{params.interface_parent_id}} = {{params.interface_id}};
            
        }
    }
"""
def generate(data):
  
  # these are parent class names
  type_names = ["Vehicle", "Pet", "Building","Celestial"]

  # these map parent class names to potential child class names
  sub_types = {"Vehicle": ["Car", "Skateboard", "Bicycle", "HotAirBalloon", "Skooter", "Skis", "Wheelchair", "Truck", "Motorcycle", "SnowShoes"],
               "Pet": ["Dragon", "Dog", "Gerbil", "Hamster", "Cat", "Snake"],
               "Building": ["Hospital", "House", "School", "Restaurant", "Tavern", "Inn", "Hotel", "Shop"],
               "Celestial": ["Star", "Planet", "Galaxy", "Moon", "Asteroid", "Comet", "Nebula", "Meteor", "BlackHole"]
              }

  # this maps parent class names to potential method names  
  type_methods = {"Vehicle": ["move", "stop", "accelerate", "enter", "exit", "slide", "crash", "skid", "jerk", "slow"],
               "Pet": ["eat", "play", "jump", "run", "emote", "blink", "claw", "hide"],
               "Building": ["open", "close", "lightsOn", "lightsOut", "alarm", "burn"],
               "Celestial": ["explode", "shimmer", "rotate", "phase", "shrink", "expand"]
              }

  # this makes a list of maps of interface names to methods
  interfaces = [{"name": "Drawable", "methods": ["draw", "paint", "outline"]},
              {"name": "Transformer", "methods": ["toPerson", "toCar", "toPlane", "toCloud", "toVegetable"]},
              {"name": "Teleporter", "methods": ["beam", "tesseract", "breach", "hyperwarp"]},
             ]  
    
  
  
  # Randomize scenario positions

  # select an interface
  random.shuffle(interfaces)
  # create the type
  interface = interfaces[0]['name']
  data['params']['interface_type'] = interface
  # create the id for the type
  interface_id = interface.lower()
  data['params']['interface_id'] = interface_id

  #get the methods for the chosen interface
  i_methods = interfaces[0]['methods']
  #randomly select one of the methods
  random.shuffle(i_methods)
  interface_method = i_methods[0]
  data['params']['interface_method'] = interface_method
  
  random.shuffle(type_names)
  
  parent = type_names[0]
  data['params']['parent_type'] = parent
  parent_id = parent.lower()
  data['params']['parent_id'] = parent_id
  child_types = sub_types[parent]
  random.shuffle(child_types)
  
  child_type = child_types[0]
  data['params']['child_type'] = child_type
  
  child_id = child_type.lower()
  data['params']['child_id'] = child_id
  
  child_interface_id = child_id + interface
  data['params']['child_interface_id'] = child_interface_id
  child_parent_id = child_id + parent
  data['params']['child_parent_id'] = child_parent_id
  interface_parent_id = interface_id + parent
  data['params']['interface_parent_id'] = interface_parent_id

  # get the methods for the class
  p_methods = type_methods[parent]
  # randomly select one of them to have
  random.shuffle(p_methods)
  p_method = p_methods[0]
  
  data['params']['parent_method'] = p_method
  
  # create correct options
  correct1 = interface + " x = " + child_id + ";"
  correct2 = parent + " x = " + child_id + ";"
  correct3 = interface + " x = (" + interface + ")" + interface_parent_id + ";"
  correct4 = interface + " x = (" + child_type + ")" + interface_parent_id + ";"
  correct5 = child_type + " x = (" + child_type + ")" + interface_parent_id + ";"
  correct6 = child_type + " x = (" + child_type + ")" + interface_id + ";"
  correct7 = child_type + " x = (" + child_type + ")" + child_parent_id + ";"
  correct8 = parent + " x = (" + child_type + ")" + interface_id + ";"
  correct9 = parent_id + "." + p_method + "();"
  correct10 = child_id + "." + p_method + "();"
  correct11 = child_id + "." + interface_method + "();"
  correct12 = interface_id + "." + interface_method + "();"

  # put the correct answers into a list
  correct_answers = [correct1,correct2,correct3,correct4,correct5,correct6,correct7,correct8,correct9,correct10,correct11,correct12]
  
  # shuffle the list to randomize which ones are used.
  random.shuffle(correct_answers)
 
  # create incorrect options
  incorrect2 = child_type + " x = (" + child_type + ")" + parent_id + ";"
  incorrect3 = interface + " x = " + interface_parent_id + ";"
  incorrect4 = interface + " x = (" + child_type + ")" + parent_id + ";"
  incorrect5 = child_type + " x = " + interface_parent_id + ";"
  incorrect6 = child_type + " x = " + interface_id + ";"
  incorrect7 = child_type + " x = " + child_parent_id + ";"
  incorrect8 = parent + " x = " + interface_id + ";"
  incorrect9 = interface_parent_id + "." + interface_method + "();"
  incorrect10 = child_parent_id + "." + interface_method + "();"
  incorrect11 = interface_parent_id + "." + interface_method + "();"
  incorrect12 = "(("+parent+")"+parent_id + ")." + interface_method + "();"

  # make them a list
  incorrect_answers = [incorrect2,incorrect3,incorrect4,incorrect5,incorrect6,incorrect7,incorrect8,incorrect9,incorrect10,incorrect11,incorrect12]

  # shuffle the list to randomize which ones are used.
  random.shuffle(incorrect_answers)
  
  # randomly decide how many will be correct
  num_correct = (int)(random.random()*4) + 1

  # put the correct and incorrect answers to select from
  # this gets randomized by the question system after the list is returned.
  for i in range(6):
      j = i + 1
      k = num_correct - i
      if i < num_correct:
        data['params']['c' + str(j)] = "true"
        data['params']['answer'+ str(j)] = correct_answers[i]
      else:
        data['params']['c' + str(j)] = "false"
        data['params']['answer'+ str(j)] = incorrect_answers[k]
  



