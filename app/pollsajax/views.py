from django.views import generic
from app.polls.models import Question


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'pollsajax/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:3]