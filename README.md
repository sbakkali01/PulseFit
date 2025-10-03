# PulseFit
An application that allows the user to define workouts with exercises.
The current scope is only for weightlifting and calisthenics ( body weight exercises )

# Motivation

Most applications that helps to organize and track your workouts lack the ability to give full ownership to the 
design and dispositions of one's workout.
This app aims to fix that by creating the basic features to allow full ownership over the user's workout. 

## 📖 Learnings

Appart from functional value ( for my own workouts )  this application will mostly be used for learning purposes. 
The idea is to develop a fullstack app from scratch without the help of any LLM. Throughtout the developement of 
this app I have mostly learned about :
- To be filled

## 🖥️ Tech Stack

The tech stack used here is : 

- FastAPI : for an easy to use asynchronous web application
- Angular : a TS frontend framework
- PostgreSQL : one of the best relational SQL database

## 🚀 MVP 

- The user can create a workout 
- A workout contains one or more exercises separated by time durations : the workout layout can be changed
- Exercises that have certain characteristics : 
  - Name
  - Description
  - Special tags possibilities : can it be done one one leg / arm , inclined , weighted ( we don't want to create an 
    exercise for inclined , one arm/legged , ... ) tags do the trick : they can be selected when added to a workout 
    (they are optional) but we still need to define which tags can each exercise have ( for instance you cannot do a 
    one legged bicep curl ...) 
  - Body parts targeted ( body parts can contain other body parts )
  - Primary and secondary body part targeted

## 🔥 Additional functionalities 

- Login / signup interface with email validation 
- ability to let users propose new exercises that will then go through a curation of pipline to see if it already 
  exists / can already be seen as a mixture of preexisting exercises. If not the exercises will be inspected and 
  then added in the main database.
- Ability to see the stats of your collegues that use the app ( you can subscribe to their account ). Possibility to 
  see their workouts ( if they are flagged as public ).
- A stats dashboard where you can see a graph with metrics across time for each exercise ( the metric can be weight ,
  reps , both , ... ) e.g. : the amount of kilos you can bench press (on the Y axis) the time (on the X axis) in 
  days (each day corresponding to a workout day of course not all days)


## Routes

This section details what each route primarily does , and the features it will include.

| Route               | Current usage                                                                        | Future features                              |
|---------------------|--------------------------------------------------------------------------------------|----------------------------------------------|
| /                   | Entry point of the application : a greating                                          | A login / signup page                        |
| /exercises          | List of all exercises                                                                | Ability to filter exercises by targeted body parts , a search bar with name |
| /create-exercise    | A page to create an exercise                                                         |                                              |
| /workouts           | List of all the current workouts                                                     | A nice way to modify the workout ( rearrage exercises and pauses order , add new exercise |
| /create-workout     | A page to add a workout                                                              |                                              |
| /in-progress        | Page of the current workout : a workout that has been selected on the / workout page | A more interactive page , no reordering of the workout can be done here |
| /stats/{workout_id} | Get the stats for each workout                                                       |                                                                         |

