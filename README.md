# thtran.com

[https://thtran.com][thtran]

This is the source for my [personal site][thtran]!

## Framework
This is a static website powered by [Flask](http://flask.pocoo.org/) and hosted by [Github Pages](https://pages.github.com/).

(Shoutout to [Armin Ronacher](http://lucumr.pocoo.org/) for making such an awesome framework and [Github](https://github.com) for letting us host our sites for free!)

## Workflow
I use [Github](https://github.com) (obviously :P) to version control and deploy this site.
- app: Development branch.
- master: Production branch.

### Setting up

Install the necessary Python packages (requires Python 2.7 with pip):

```
# After activating the virtualenv
$ pip install -r requirements.txt
```

### Building the site

To run the local development server

```
$ python manage.py runserver
```

Browse to `http://localhost:5000/` to view the site.

To build the static version of the site:

```
$ python manage.py build
```

This will build the static site to the `build/` directory.

### Deployment

To deploy to GitHub Pages:

```
$ python manage.py deploy
```

This will build the site, commit to the `master` branch, and push to GitHub.

### Notes

- This site is a continuous WIP: I'll keep adding more features and content as I develop myself :)

[thtran]: https://thtran.com
