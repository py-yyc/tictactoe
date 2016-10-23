# TicTacToe

This will be a multi-session project where we implement tictactoe.

## instructions

* Please use python 2.7
* make a virtual environment
* code in a branch

### virtual environment

```bash
sudo pip install virtualenv # if not already installed
virtualenv venv
source venv/bin/activate
```

### git branch

To create a branch do the following.

```bash
git pull https://github.com/py-yyc/tictactoe.git
git checkout -b your_names
```

### Your Own Fork

If you want to work off your own fork, do the above. Next, click the
"Fork" button in the upper-right on the GitHub page. Then you must add
your new fork as a remote:

```bash
git remote add github https://github.com/<your_username>/tictactoe.git
git fetch github
git branch --set-upstream your_names github/your_names
```

## session 1

You must write tests first! Fill in `test_ttt.py` before implementing
`ttt.py`.

Feel free to change any and all design, but for this first assignment
please implement `game_state()` that returns something to do with `states`.
