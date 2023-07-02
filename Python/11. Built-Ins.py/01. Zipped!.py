N, X = map(int, input().split())

scores_lists = []
for _ in range(X):
    scores = list(map(float, input().split()))
    scores_lists.append(scores)

for student_score in zip(*scores_lists):
    print(f'{sum(student_score)/len(student_score):.1f}')