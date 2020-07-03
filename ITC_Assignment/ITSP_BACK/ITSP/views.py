from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response, status
from .serializers import itsp_teamSerializer

# Create your views here.
from .models import itsp_team


def itsp_home(request):
    queryset = itsp_team.objects.all()
    context = {
        'itsp_teamname': queryset
    }
    return render(request, 'ITSP/itsp_home_page.html', context)


def dynamic_view(request, my_id):
    # obj = get_object_or_404(itsp_team, id=my_id)
    obj = itsp_team.objects.filter(Team_ID=my_id)
    context = {
        'object': obj
    }
    return render(request, "ITSP/team_details.html", context)


def landing_page(request):
    return render(request, "index.html")


class itsp_team_API(APIView):
    def get(self, request):
        itsp_team_r = itsp_team.objects.all()
        serializer = itsp_teamSerializer(itsp_team_r, many=True)
        return Response(serializer.data)

    def post(self):
        pass
