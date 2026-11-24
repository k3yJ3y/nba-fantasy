from nba_api.stats.static import teams

from clients.team_dto import TeamDto


class TeamsService:
    def get_teams(self) -> list[TeamDto]:

        all_teams = teams.get_teams()
        all_teams_dto = [TeamDto.model_validate(team) for team in all_teams]
        print(type(all_teams_dto))
        return all_teams_dto

    def get_team(self, id):
        print("getting team by some id")