import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'fpl_web_app_project.settings')

import django
django.setup()
import asyncio
import aiohttp
from fpl import FPL
from fplhelp.models import TeamFDR


def populate():

    # Get fixture difficulty ratings
    async def main():
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            fdr = await fpl.FDR()

            # Populate database
            for team, position in fdr.items():
                t = TeamFDR.objects.get_or_create(name=team, allAway=position['all']['A'],
                                                  allHome=position['all']['H'],
                                                  goalkeeperAway=position['goalkeeper']['A'],
                                                  goalkeeperHome=position['goalkeeper']['H'],
                                                  defenderAway=position['defender']['A'],
                                                  defenderHome=position['defender']['H'],
                                                  midfielderAway=position['midfielder']['A'],
                                                  midfielderHome=position['midfielder']['H'],
                                                  forwardAway=position['forward']['A'],
                                                  forwardHome=position['forward']['H'],
                                                  )
                t.save()


# Start execution here
if __name__ == '__main__':
    print('Starting 2022 season population script...')
    populate()