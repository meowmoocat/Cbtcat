from datetime import datetime

from django.shortcuts import render
from django.views.generic import View

from ..models import CbtcatUser, L1A, Lvl1UserData


class Intro(View):
    template_name = 'intro.html'

    def post(self, request):
        user = request.user
        cbtcat_user = CbtcatUser.objects.get(username=user.username)
        answers, created = L1A.objects.get_or_create(username=user.username, finished=False)
        question = answers.current_question
        option = request.POST['options']

        if option == 'catastrophising' and question == 1:
            answers.current_question = question+1
            feedback = 'Correct'
        elif option == 'mindreading' and question == 2:
            answers.current_question = question + 1
            feedback = 'Correct'
        elif option == 'labelling' and question == 3:
            answers.current_question = question + 1
            feedback = 'Correct'
        elif option == 'allornothing' and question == 4:
            answers.current_question = question + 1
            feedback = 'Correct'
        elif option == 'overgeneralisation' and question == 5:
            user_data = Lvl1UserData.objects.get(table_created=True)
            if L1A.objects.filter(username=cbtcat_user.username, finished=True).exists():
                finished = user_data.total_times_finished
                user_data.total_times_finished = finished + 1
            else:
                finished = user_data.total_times_finished
                user_data.total_times_finished = finished + 1
                unique_finishes = user_data.num_unique_users_completed
                user_data.num_unique_users_completed = unique_finishes + 1
            user_data.save()
            answers.current_question = question + 1
            answers.finished_on = datetime.now()
            answers.finished = True
            answers.save()
            cbtcat_user.current_level = 2
            cbtcat_user.save()
            return render(request, 'index.html', {'level': cbtcat_user.current_level})
        else:
            feedback = 'Try again'

        answers.save()
        return render(request, self.template_name, {"question": answers.current_question, "feedback": feedback})

    def get(self, request):
        user = request.user
        cbtcat_user = CbtcatUser.objects.get(username=user.username)
        answers, created = L1A.objects.get_or_create(username=cbtcat_user.username, finished=False)
        user_data, created = Lvl1UserData.objects.get_or_create(table_created=True)

        if L1A.objects.filter(username=cbtcat_user.username, finished=True).exists():
            started = user_data.total_times_started
            user_data.total_times_started = started + 1
        else:
            started = user_data.total_times_started
            user_data.total_times_started = started + 1
            unique_starts = user_data.num_unique_users_started
            user_data.num_unique_users_started = unique_starts + 1
        user_data.save()
        return render(request, self.template_name, {"question": answers.current_question, "feedback": ""})
