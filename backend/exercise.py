class Exercise:

    def __init__(self, name, description, equipment, targeted_muscles):
        self.name = name
        self.description = description
        self.equipment = equipment
        self.targeted_muscles: list = targeted_muscles


exercises = [Exercise(
    "Pull Up",
    "A pulling exercise to work your lats and biceps",
    "pull-up bar",
    ["lats", "biceps", "brachialis", "forearms"]
)

,Exercise(
    "Bench Press",
    "A compound pushing exercise that targets the chest, shoulders, and triceps",
    "barbell and bench",
    ["chest", "triceps", "front deltoids"]
)

,Exercise(
    "Squat",
    "A fundamental lower-body exercise that builds strength in the legs and core",
    "barbell or bodyweight",
    ["quadriceps", "glutes", "hamstrings", "core"]
)

,Exercise(
    "Overhead Press",
    "A pressing movement to strengthen the shoulders and triceps",
    "barbell or dumbbells",
    ["shoulders", "triceps", "upper chest", "core"]
)

,Exercise(
    "Lunges",
    "A unilateral lower-body exercise that improves balance and leg strength",
    "bodyweight or dumbbells",
    ["quadriceps", "glutes", "hamstrings", "calves"]
)]
