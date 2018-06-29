#import cmd

#class hello(cmd.Cmd):
#    def do_hello(self,person):
#        """
#        hello [person]
#        greet the Named Person
#        """
#        if person:
#            print("hi",person)
#        else:
#            print("You are High")
#
 #       def do_EOF(self,line):
   #         return True
  #      def postloop(self):
 #           print()
#hello().cmdloop()

from .news import do_news
from .quote import do_quote
from .wallpaper import do_wallpaper



