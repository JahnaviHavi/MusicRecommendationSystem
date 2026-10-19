import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define input variables
mood = ctrl.Antecedent(np.arange(0, 11, 1), 'mood')         # 0 = Sad, 10 = Happy
activity = ctrl.Antecedent(np.arange(0, 11, 1), 'activity') # 0 = Studying, 10 = Workout
language = ctrl.Antecedent(np.arange(0, 11, 1), 'language') # 0 = Regional, 10 = English
genre = ctrl.Antecedent(np.arange(0, 11, 1), 'genre')       # 0 = Classical, 10 = Pop/Rock
tempo = ctrl.Antecedent(np.arange(0, 201, 1), 'tempo')      # BPM: 0–200
recommendation = ctrl.Consequent(np.arange(0, 11, 1), 'recommendation')

# Membership functions (Triangular)
mood['sad'] = fuzz.trimf(mood.universe, [0, 0, 5])
mood['neutral'] = fuzz.trimf(mood.universe, [2, 5, 8])
mood['happy'] = fuzz.trimf(mood.universe, [5, 10, 10])

activity['study'] = fuzz.trimf(activity.universe, [0, 0, 5])
activity['relax'] = fuzz.trimf(activity.universe, [2, 5, 8])
activity['workout'] = fuzz.trimf(activity.universe, [5, 10, 10])

language['regional'] = fuzz.trimf(language.universe, [0, 0, 5])
language['hindi'] = fuzz.trimf(language.universe, [2, 5, 8])
language['english'] = fuzz.trimf(language.universe, [5, 10, 10])

genre['classical'] = fuzz.trimf(genre.universe, [0, 0, 5])
genre['jazz'] = fuzz.trimf(genre.universe, [2, 5, 8])
genre['poprock'] = fuzz.trimf(genre.universe, [5, 10, 10])

tempo['slow'] = fuzz.trimf(tempo.universe, [0, 40, 80])
tempo['moderate'] = fuzz.trimf(tempo.universe, [60, 100, 140])
tempo['fast'] = fuzz.trimf(tempo.universe, [120, 160, 200])

recommendation['low'] = fuzz.trimf(recommendation.universe, [0, 0, 5])
recommendation['medium'] = fuzz.trimf(recommendation.universe, [3, 5, 7])
recommendation['high'] = fuzz.trimf(recommendation.universe, [5, 10, 10])

# Define 17 fuzzy rules
rules = [
    ctrl.Rule(mood['happy'] & activity['workout'] & tempo['fast'], recommendation['high']),
    ctrl.Rule(mood['sad'] & tempo['slow'] & genre['classical'], recommendation['medium']),
    ctrl.Rule(activity['study'] & tempo['fast'], recommendation['low']),
    ctrl.Rule(genre['jazz'] & language['hindi'], recommendation['medium']),
    ctrl.Rule(mood['neutral'] & genre['poprock'] & tempo['moderate'], recommendation['high']),
    ctrl.Rule(language['regional'] & genre['classical'], recommendation['low']),
    ctrl.Rule(mood['happy'] & genre['poprock'] & tempo['moderate'], recommendation['high']),
    ctrl.Rule(mood['sad'] & activity['study'], recommendation['medium']),
    ctrl.Rule(activity['relax'] & tempo['slow'], recommendation['medium']),
    ctrl.Rule(activity['relax'] & tempo['fast'], recommendation['low']),
    ctrl.Rule(language['english'] & genre['poprock'], recommendation['high']),
    ctrl.Rule(language['regional'] & mood['sad'], recommendation['low']),
    ctrl.Rule(mood['neutral'] & genre['jazz'], recommendation['medium']),
    ctrl.Rule(mood['happy'] & activity['relax'] & tempo['moderate'], recommendation['high']),
    ctrl.Rule(mood['neutral'] & activity['study'], recommendation['medium']),
    ctrl.Rule(activity['workout'] & tempo['slow'], recommendation['low']),
    ctrl.Rule(language['hindi'] & genre['classical'] & tempo['moderate'], recommendation['medium']),
]

# Create and simulate fuzzy control system
recommend_ctrl = ctrl.ControlSystem(rules)
recommend_sim = ctrl.ControlSystemSimulation(recommend_ctrl)

# Example input
recommend_sim.input['mood'] = 8         # Happy
recommend_sim.input['activity'] = 10    # Workout
recommend_sim.input['language'] = 10    # English
recommend_sim.input['genre'] = 9        # Pop/Rock
recommend_sim.input['tempo'] = 150      # Fast

# Compute result
recommend_sim.compute()
print("Recommendation Score (0-10):", round(recommend_sim.output['recommendation'], 2))
# Visualize output
recommendation.view(sim=recommend_sim)
plt.title("Fuzzy Music Recommendation Output")
plt.grid(True)
plt.show()
