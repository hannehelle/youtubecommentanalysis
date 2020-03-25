import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAcB2m1Y_iGYhXjjgQ_pnmPJtZ-tRF5vYw"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        channelId="UC6iRO8qu5tdTaZgzEiCSSkA",
        moderationStatus="published",
        order="time",
        pageToken=DEVELOPER_KEY,
        textFormat="plainText"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()