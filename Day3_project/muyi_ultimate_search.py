#### This is the start of MUYI ULTIMATE SEARCH code #########

print('''

              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
          jgs  _/_______\_
              /___________\


''')
print("Welcome to MUYI ULTIMATE SEARCH.")
print("Your mission is to find the GOLDEN TROPHY.")

choice1 = input("\n You and your friends are at the enterance of the Enchanted Garden,\n a magical place filled with blooming flowers and friendly creatures.\n There are two gates here; blue and red. type blue or red below. \n \n").lower()

if choice1 == "blue":
  choice2 = input("\n Welcome to the Enchanted Garden.\n You can decide to swim through the river or \n walk on the bridge to get to the illustration map. \n type river or bridge. \n \n ").lower()

  if choice2 == "bridge":
    choice3 = input("\n You made it to the Map Chamber!.\n As you entered the chamber you were welcomed by three hostees each holding \n a tray containing iPad, iPhone, and scroll.\n Type iPad or iPhone or scroll to choose your prefered tool. \n \n ").lower()
    if choice3 == "scroll":
      print("\n You made the right choice. \n The map will help you locate the golden trophy. \n \n YOU WIN!!!")
    else:
      print("\n Wrong tray! You have been arrested by the garden police. \n This is now your new home. \n \n GAME OVER")

  else:
    print("\n You have been swallowed by a Dorphin. \n \n GAME OVER!")

else:
  print("Wrong gate! You have been deported. GAME OVER!")
