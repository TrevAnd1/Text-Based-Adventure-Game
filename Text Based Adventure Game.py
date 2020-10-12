print('Welcome to my first game!')
name = input('What is your name? ')
age = input('How old are you? ')

print('Hello', name, 'you are', age, 'years old.')

health = 10


if age >= '16':
  print('You are old enough to play!')
  wants_to_play = input('Do you want to play a game? (yes/no) ').lower()

  if wants_to_play == 'yes':
    print("Awesome, let's begin!")
    print('You are starting with', health, 'health.')
    
    ans = input('There are two paths you can take, you can either take the left door or the right door. Which do you want to take? (left/right)')
    if ans == 'right':
     print("As you begin your journey down the path you see a baby gazelle calmyly grazing on some grass on the side the of the path. You decide to take out your camera and snap a quick pic. Oops, you forgot the flash was on, and now it's blinded and angry. You start to feel the ground tremble as, out of the corner of your eye, you see a stampede of gazelles coming right at you. I will leave the rest for your imagination :) You lost 5 health.")
     ans = input('You come up to a large pond, you can either go through the pond or go around. Which do you want to do? (through/around)')
 
     health -= 5

    if ans == 'left':
      ans = input('You barely make it across the broken bridge, nice! You come up to a large pond, you can either go through the pond or go around. Which do you want to do? (through/around)')
    
    if ans == 'through':
        print('You send a thank you thought to your elementary school swimming coach as you doggie paddle your way across the pond!')
    elif ans == 'around':
        print('What you thought might have been the safer option turned out to be the exact opposite as you step on the foot of a baby gazelle on your way around. You start to feel the ground tremble as, out of /the corner of your eye, you see a stampede of gazelles coming right at you. I will leave the rest for your imagination :) You lost 5 health.')

        health -= 5

    if health <= 0:
      print('You have 0 health, game over...')
    else:
      ans = input('You realize you are very thirsty as you come across a random house on the edge of the pond. Do you stop in the house for a quick glass of water or do you fight through it and head towards the helicopter waiting to pick you up? (drink/get me out)')
      if ans == 'drink':
        print('Well that was refreshing! As you relax by the fire, drying off from the swim and replenishing your thirst, a stampede of gazelles come rampaging right in front of the helicopter! After the glass, you safely walk over to the helicopter and make it out alive. Well done!')
      elif ans == 'get me out':
        print('As you walk over the helicopter, you start to feel the ground tremble as, out of the corner of your eye, you see a stampede of gazelles coming right at you. I will leave the rest for your imagination :) You lost 5 health.')
        
        health -= 5

         
      if health <= 0:
       print('You have 0 health, game over...')
      else:
        print('Congrats, you survived!')

  elif wants_to_play == 'no':
    print("Fine, I didn't want to play with you anyways. Game over, I guess...")

elif age <= '16':
 print("Damn, you're young. You don't deserve to play this game. This game is too cool for you. Go play Minecraft or something, weirdo.")

          
