from package import (
do_news,do_quote,do_wallpaper,do_movies,do_youtube
)


import cmd
import sys
class FirstCmdApplication(cmd.Cmd):
    try:
        intro = "Welcome {username}!".format(username=sys.argv[1])
    except IndexError:
        print("Please provide your username!")
        exit()
    prompt = 'Cli: '

    def do_youtube(self,arg):
        "youtube video"
        do_youtube()

    def do_history(self, arg):
        "not working"
        print(self._history)

    def do_news(self, arg):
        "Read today's news"
        do_news()

    def do_movies(self,title):
        "get movies ratings n info"
        do_movies(title)

    def do_quotes(self, arg):
        "Read quote of the day"
        do_quote()
    def do_wallpaper(self,arg):
        "Display Wallpaper"
        do_wallpaper()



    def do_exit(self, arg):
        "Exit the application"
        return -1

    def precmd(self, line):
        """ This method is called after the input but before
            it has been interpreted. If you want to modify the input line
            before execution (for example, variable substitution) do it here.
        """
        if line != '':
            self._history += [ line.strip() ]
        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.
           If you want to do some post command processing, do it here.
        """
        return stop

    def preloop(self):
        "Initialization before prompting user for commands"
        cmd.Cmd.preloop(self)
        self._history = []

    def postloop(self):
        "Take care of any unfinished business."
        print("Exiting...")
        cmd.Cmd.postloop(self)

if __name__=='__main__':
    FirstCmdApplication().cmdloop()
