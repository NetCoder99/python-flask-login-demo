import json
import os

from flask import Blueprint
from github import Github, Auth, RateLimit

gitapi_blueprint = Blueprint('gitapi_blueprint',__name__,template_folder='templates',static_folder='static')

@gitapi_blueprint.route('/repositories_api', methods=['GET'])
def repositories_api():
    print('repositories_api - started')
    git_auth = Auth.Token(os.getenv('GIT_TOKEN'))
    git_obj  = Github(auth=git_auth)

    rate_lmit:RateLimit = git_obj.get_rate_limit()

    for repo in git_obj.get_user().get_repos():
        print(repo.name)

    github_url   = 'https://github.com/'
    github_repos = 'https://github.com/NetCoder99?tab=repositories'
    rtn_data = {
        'github_url' : github_url
    }
    return json.dumps(rtn_data)


#         return json_data['products']
#
#
# from github_procs import Github
#
# # Authentication is defined via github_procs.Auth
# from github_procs import Auth
#
# # using an access token
# auth = Auth.Token("access_token")
#
# # First create a Github instance:
#
# # Public Web Github
# g = Github(auth=auth)
#
# # Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", auth=auth)
#
# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)
