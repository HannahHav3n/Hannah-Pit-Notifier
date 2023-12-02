# Hannah Notifier
> *A windows Hypixel pit event notifier*

# How does it work?
What it does is it uses the `https://brookeafk.com` api, it decodes the data and saves it to a file called Events.txt
it then opens the file and appends it all to a list for later usage, the while true loop then checks if the current time
is equal to any of the times in the event times and if it is then it will append the event to a seperate list so it does
not trigger again because it will be in the list for 60 seconds (because time), it also prints a notification and spawns
a windows notification of the event.

# Instillation
1. Download the repository
2. Run the following command in a shell in the folder you dowloaded `pip install -r requirements.txt`
3. Run `python 'Hannah Notifier.py'`
4. You have installed Hannah notifier

### OR

Run the exe

# Shoutout
Original site and api maker: `https://brookeafk.com`

# Media
If you want to make a video on this please link my youtube `https://www.youtube.com/channel/UCag7cztDCgGUYX0Vu6tuu6A`
and my github `https://github.com/HannahHav3n` <3

# Todo
1. Add lookup player stats
2. Add upcoming events
