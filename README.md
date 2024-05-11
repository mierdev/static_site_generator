# SSG (Static Site Generator)

My second Boot.dev guided project! 

Guided projects are designed to get you *out* of tutorial hell, by writing a ton of code and giving you challenges to solve on your own (you are given a few hints, but the rest is on you and Google).

## About Book Bot

A static site generator takes raw content files (like Markdown and images) and turns them into a static website of HTML and CSS files. Static sites are quite popular for blogs and other content-heavy websites because they're lightning-fast, secure, and easy to host.

#### STATIC VS DYNAMIC SITES

A static site is what it sounds like... _static_. No matter who is interacting with the site, the content is always the same. You can not log in, you can't leave comments, or upload files to a static site. You would need a dynamic site for that stuff, which is usually powered by a database and a custom web server. 

## Pre-Requisites

- Git
- GitHub
- Python 3.11+
- A unix-like shell (bash, zsh, fish, etc.)

## Clone Project & Open With Python Server

In your CLI, use the command:

```bash
git clone git@github.com:mierdev/static_site_generator.git
```

Then navigate to the root of static_site_generator project and use the following command:

```bash
python server.py --dir public
```

Open your browser and paste the URL of your server (probably http://localhost:8888) into the address bar. You should see the project rendered as a web page!
