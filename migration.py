import requests
import csv
import sys


class InstaMigration():
    def __init__(self, user, token='2754289.513db26.7f761da8174b4f75ab8b6f741d950c9c'):
        BASE_URL = 'https://api.instagram.com/v1/users'
        user_url = '{}/search?q={}&access_token={}&count=1'.format(BASE_URL, user, token)
        request = requests.get(user_url)
        json = request.json()

        if request.status_code == 200:
            if json.get('data'):
                # get the user id to continue with the migration
                user_id = json.get('data')[0].get('id')

                self.following = ['You Follow:']
                self.url = '{}/{}/follows?access_token={}'.format(BASE_URL, user_id, token)
            else:
                print "------------------------------------------"
                print "Could not find the user '{}'".format(user)
                print "------------------------------------------"
                sys.exit()
        else:
            print "--------------------------"
            print "Error looking for the user"
            print "--------------------------"
            sys.exit()

    def make_migration(self, next_url=None):
        """
        Make the Instagram request and get json and next url if have pagination
        """
        request = requests.get(next_url if next_url else self.url)

        # check if is success code (200)
        if request.status_code == 200:
            json = request.json()
            next_url = json.get('pagination').get('next_url')
            self.get_users_name(json, next_url)
        else:
            print "------------------------------"
            print "The request was not successful"
            print "------------------------------"
            sys.exit()

    def get_users_name(self, json, next_url):
        """
        Get each username and put in a csv file
        """
        for user in json.get('data'):
            self.following.append(user.get('username'))

        # if have next url continue to fetch the users
        if next_url:
            self.make_migration(next_url)
        else:
            self.create_csv_file()
            print "----------------"
            print "End of migration"
            print "----------------"

    def create_csv_file(self):
        """
        Create the csv file with the users name
        """
        with open('instagram-users-migration.csv', 'w') as fp:
            a = csv.writer(fp, delimiter=',')
            for user in self.following:
                a.writerow([user])

