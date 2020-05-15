from datetime import datetime

from django.shortcuts import render
from django.views.generic import View

from ..models import CbtcatUser, L3Ans, Lvl3UserData


class AllOrNothing(View):
    template_name = 'all_or_nothing.html'

    def post(self, request):
        user = request.user
        cbtcat_user = CbtcatUser.objects.get(username=user.username)
        answers, created = L3Ans.objects.get_or_create(username=user.username, finished=False)
        question = answers.current_question
        feedback = ''

        if question == 1:
            answer = request.POST['options']
            if answer == 'allornothing':
                feedback = 'Correct'
                answers.current_question = question + 1
            else:
                feedback = 'Try again'

        elif question == 2:
            answer = request.POST['answer2']
            answer = answer.lower()
            if len(answer) < 20:
                feedback = 'Try write a little more\n'
            elif 'climb' not in answer and 'balance' not in answer and 'embarrass' not in answer and 'bad' not in answer:
                feedback = 'Think about it a little more'
            else:
                feedback = 'Correct'
                answers.current_question = question + 1

        elif question == 3:
            answer = request.POST['answer3']
            answer = answer.lower()
            if len(answer) < 7:
                feedback = 'Try write a little more\n'
            elif 'fell' not in answer and 'fall' not in answer and 'slipped' not in answer and 'climb' not in answer:
                feedback = 'Think about it a little more'
            else:
                feedback = 'Correct'
                answers.current_question = question + 1

        elif question == 4:
            answer = request.POST['answer4']
            answer = answer.lower()
            if len(answer) < 25:
                feedback = 'Try write a little more\n'
            elif 'high' not in answer and 'perfectly' not in answer and 'balanced' not in answer and 'good' not in answer:
                feedback = 'Think about it a little more'
            else:
                feedback = 'Correct'
                answers.current_question = question + 1

        elif question == 5:
            answer = request.POST['answer5']
            answer = answer.lower()
            if len(answer) < 4:
                feedback = 'Try write a little more\n'
            elif 'feel' not in answer:
                feedback = 'Think about it a little more'
            else:
                feedback = 'Correct'
                answers.current_question = question + 1

        elif question == 6:
            answer = request.POST['answer6']
            answer = answer.lower()
            if len(answer) < 10:
                feedback = 'Try write a little more\n'
            elif 'high' not in answer and 'perfectly' not in answer and 'balanced' not in answer and 'good' not in answer:
                feedback = 'Think about it a little more'
            else:
                answers.current_question = question + 1

                user_data = Lvl3UserData.objects.get(table_created=True)
                if L3Ans.objects.filter(username=cbtcat_user.username, finished=True).exists():
                    finished = user_data.total_times_finished
                    user_data.total_times_finished = finished + 1
                else:
                    finished = user_data.total_times_finished
                    user_data.total_times_finished = finished + 1
                    unique_finishes = user_data.num_unique_users_completed
                    user_data.num_unique_users_completed = unique_finishes + 1
                user_data.save()
                answers.finished_on = datetime.now()
                answers.finished = True
                answers.save()
                if cbtcat_user.current_level == 3:
                    cbtcat_user.current_level = 4
                cbtcat_user.save()
                return render(request, 'index.html', {'level': cbtcat_user.current_level})

        answers.save()
        return render(request, self.template_name, {"question": answers.current_question, "feedback": feedback})

    def get(self, request):
        user = request.user
        cbtcat_user = CbtcatUser.objects.get(username=user.username)
        answers, created = L3Ans.objects.get_or_create(username=cbtcat_user.username, finished=False)
        user_data, created1 = Lvl3UserData.objects.get_or_create(table_created=True)

        if L3Ans.objects.filter(username=cbtcat_user.username, finished=True).exists():
            started = user_data.total_times_started
            user_data.total_times_started = started + 1
        else:
            started = user_data.total_times_started
            user_data.total_times_started = started + 1
            unique_starts = user_data.num_unique_users_started
            user_data.num_unique_users_started = unique_starts + 1
        user_data.save()
        return render(request, self.template_name, {"question": answers.current_question, "feedback": ""})
