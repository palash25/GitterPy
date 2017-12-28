# GitterPy [WIP]

## Whats this?
A simple command line client to interact with the Gitter API.

## Why this?
Like a lot of developers I use gitter on a daily basis, but I also hate using it. Slow loading of rooms, messages from different rooms mixing up together while switching rooms(especially if you're on a slow network) and many other glitches, but I still have to use it everyday. This is an attempt to solve this problem (also an opportunity to learn [click](http://click.pocoo.org/) which is a pretty cool framework if you want to build cli applications).

## Why use this?
- If you hate gitter but use it everyday
- If you love cli tools and spend a lot of time on your terminal
- If you have a slow internet connection

## Wanna see it in action?
![cowaps in action](https://raw.githubusercontent.com/palash25/gitter-cli/master/assets/gitterpy.gif)

## Requirements
- **Click**
- **Requests**

## Installation
```
git clone <this-repo>
cd gitter-cli
pip install --editable .
```

## Usage
Type `gitterpy --help` to get the help page which looks something like this
```
  ###############Welcome to GitterPy##############

  Your command line client to interact with gitter
  ################################################

    This tool can fetch and post info to gitter

  ##################User Manual###################

  Currently this tool provides two commands `get` and `post`

  Fetching user info: gitterpy get [--info] [argument]

  The info argument can be:

  1) [u] -> To fetch user's profile

  2) [r] -> To fetch the rooms

  3) [g] -> To fetch groups

  4) [m] -> To fetch messages

  Post a message to a room: gitterpy post [--message] [text]

  [text] -> It is the message you want to post in enclosed by quotes

```

## Contributing
Right now this is a work in progress and pull requests are not welcome but it will soon be open for other contributors to hack on and make it better.

## To Do
- Better JSON traversing
- Add a storage module
- Finding messages by IDs
- Better printing and formatting


