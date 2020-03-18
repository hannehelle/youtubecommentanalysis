# import os

# import googleapiclient.discovery

# # from apidiscovery import build

# def main():
#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

#     api_service_name = "youtube"
#     api_version = "v3"
#     DEVELOPER_KEY = "AIzaSyAcB2m1Y_iGYhXjjgQ_pnmPJtZ-tRF5vYw"

#     youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, developerKey = DEVELOPER_KEY)

#     request = youtube.commentThreads().list(
#         part="id, replies, snippet",
#         channelId="UCgP7BcgH2bBLDbPv0BnmmtQ",
#         moderationStatus="published",
#         order="time",
#         textFormat="plainText"
#     )
#     response = request.execute()

#     print(response)

# if __name__ == "__main__":
#     main()




#     # -*- coding: utf-8 -*-

# # Sample Python code for youtube.commentThreads.list
# # See instructions for running these code samples locally:
# # https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAcB2m1Y_iGYhXjjgQ_pnmPJtZ-tRF5vYw"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        moderationStatus="published",
        order="time",
        textFormat="plainText",
        videoId="NnZ6wIwd9Ww"
    )
    response = request.execute()

    values = response.values()

    for value in values:
        print (values['snippet'])

    #     if value == "snippet":
    #         level_1 = values['snippet']
    #         print('пройден 1 этап')
    #         for key in level_1:
    #             if key == 'topLevelComment':
    #                 level_2 = level_1['topLevelComment']
    #                 print('пройден 2 этап')
    #                 for kkk in level_2:
    #                     level_3 = level_2['snippet']
    #                     print('пройден 3 этап')
    #                     for kkkk in level_3:
    #                         if kkkk == 'textDisplay':
    #                             level_4 = level_3['textDisplay']
    #                             print (level_4)

if __name__ == "__main__":
    main()