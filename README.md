# electric_slide

**Authors**: [Nathan Moore](https://github.com/nathancmoore), [Mark Reynoso](https://github.com/markreynoso), [Megan Flood](https://github.com/musflood), [Joseph Kim](https://github.com/jjskim)

**Version**: 1.0.0

## Overview
```electric_slide``` implements artificial intelligence and machine learning to efficiently solve the classic [sliding puzzle.](https://en.wikipedia.org/wiki/Sliding_puzzle)

## Website
[Check it out](https://electric-slide.herokuapp.com)

## Getting Started
- Clone down the repository to your local machine:
```
$ git clone https://github.com/markreynoso/electric_slide.git
```
- Once your download is complete, cd into the ```electric_slide``` repository:
```
$ cd electric_slide
```
- Create a new virtual environment with Python 3 and activate it:
```
electric_slide $ python3 -m venv ENV
electric_slide $ . ENV/bin/activate
```
- Install the project in editable mode along with its testing requirements, via pip:
```
(ENV) electric_slide $ pip install -e .[testing]
```
- Test your project, via pytest:
```
(ENV) electric_slide $ py.test
```
- Begin serving your application, via the ```pserve``` command:
```
(ENV) electric_slide $ pserve development.ini --reload
```

## Routes:

| Route | Route Name | Description |
| --- | --- | --- |
| /  | home | The home page |
| /about | about | Information about the team |
| /data | data | Displays graphs of puzzle info & comparison between solving methods |
| /api/data/states | states-data | Returns number of states at each complexity level |
| /api/data/solve | solving-data | Returns time and moves required by each algorithm to solve |
| /api/shuffle | shuffle | Return a shuffled board state |
| /api/solve/tree | tree | Return a list of moves to solve the given board state, determined by the decision tree |
| /api/solve/greedy | greedy | Returns a list of moves to solve the given board state, determined by the greedy pure-heuristic algorithm |
| /api/solve/astar | astar | Returns a list of moves to solve the given board state, determined by the A* heuristic algorithm |

## Built With:

- [Pyramid Framework](https://trypyramid.com)

- [Cookiecutter-PyPackage](https://github.com/audreyr/cookiecutter)

- [Start Bootstrap](https://startbootstrap.com/template-overviews/bare/)

- [Chart.js](http://www.chartjs.org/)

## Resources
- prestoj - https://github.com/prestoj/15-puzzle/blob/master/neural_network.py.

## Change Log
- 11-02-2017 3:50pm - Updated README.
