# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 17/11/2019.
import os as opy, re

class os:

    def __getattr__(self, item):
        return item

    def __init__(self):
        if "" is not opy.environ.get('HTTP_USER_AGENT'):
            self.agent = opy.environ.get('HTTP_USER_AGENT')
        else:
            self.agent = None

        self.info = []
        self.name()
        self.name = self.info['OS']

    def name(self):
         NAME = {
                "Windows": "Windows",
							"Linux" : "Linux",
							"Unix" : "Unix",
							"Mac": "Mac",
							"Android" : "Android"

            }
         agent = str(self.agent)

         slipt1 = agent.split(")")
         slipt2 = str(slipt1).split("(")
         splits = str(slipt2).split(" ")
         for key in splits:

            if len(key) > 0:
                if NAME.get(key, None) is not None:
                    self.info = {'OS': key}
                    break
                else:
                    self.info = {'OS': "UNKNOWN"}


            else:
                self.info = {'OS': "UNKNOWN"}

         self.info.update(self.info)