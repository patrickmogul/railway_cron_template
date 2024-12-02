# Python CRON job template for Railway.com
Railway CRON job template

/app/main.py
This file hits your url and sends Hi! in our example.

/app/error.py
This file hits your url and sends Error! in our example.

We're using ntfy.sh to show the output of our request.

Setup your single run python app as main.py and configure away or use our setup with error for anything that might go wrong with a different custom endpoint. This is just an example repo and anything can be done!

# Railway Config
In the settings you only need to add the following for the start command for main.py:

`python app/main.py`

You can also setup a 2nd cron job pointing to the same repo with the error.py command:

`python app/error.py`

Then configure the cron job to run on your schedule. The fastest Railway allows is every 5 minutes with:

`*/5 * * * *`

## Railway Variable
To use our code setup the following variable:

NOTIFY_URL=https://ntfy.sh/yourendpoint

Feel free to customize the endpoint or use your own.