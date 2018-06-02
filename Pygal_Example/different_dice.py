from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequncies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequncy = results.count(value)
    frequncies.append(frequncy)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and D10s dice 50000 times"
hist.x_title = "Result"
hist.x_labels = []
for cnt in range(2, max_result + 1):
    hist.x_labels.append(cnt)

# hist.x_labels = [
#     '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
#     '16'
# ]
hist.y_title = "Frequency of Result"
hist.add('D6+D10', frequncies)
hist.render_to_file("dice_visual.svg")