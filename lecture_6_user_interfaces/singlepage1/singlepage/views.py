from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, 'singlepage/index.html')


sectionContent = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pellentesque ex nec eros hendrerit suscipit. Duis luctus ullamcorper turpis, at mollis justo rutrum quis. Maecenas condimentum erat sed leo accumsan, eget euismod tortor auctor. Proin vitae volutpat tellus. Nullam nec dui nibh. Donec nunc dui, efficitur id augue quis, iaculis vestibulum massa. Phasellus at consequat arcu. Nulla sagittis metus sem, eu egestas arcu varius vel. Maecenas bibendum maximus convallis. Sed eu vestibulum est, vel pellentesque dolor. Cras quis tortor nec diam consectetur bibendum. Integer porta enim at tellus pharetra consectetur.",
                  "Pellentesque nunc dolor, convallis non nisi at, eleifend ultricies ante. Pellentesque at orci elementum, faucibus lacus ac, faucibus erat. Nulla sodales, tortor non ullamcorper efficitur, nulla nisi maximus felis, sed convallis elit lorem sodales felis. Proin non viverra ante. Pellentesque auctor nisi blandit neque pulvinar, eget facilisis justo dapibus. Maecenas eu magna luctus, viverra diam nec, pharetra nisl. Donec faucibus condimentum diam. Nullam sed porta elit, eu dapibus velit. Proin tempus magna id dui viverra, sit amet pulvinar tortor suscipit. Aenean vitae est tempor, interdum sem et, accumsan lectus. Cras dictum justo et mi dignissim, non posuere augue volutpat. Vestibulum vitae quam nec metus facilisis dignissim. Maecenas venenatis purus vitae nisl lobortis, sit amet porta enim venenatis. Nam sagittis sapien sollicitudin nisi ullamcorper varius.",
                  "Nulla lobortis nec eros et pretium. Cras eu rhoncus metus. Vestibulum dolor justo, luctus a velit nec, sagittis sagittis lectus. Nulla a pretium massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras quis augue vel turpis egestas pulvinar ut sit amet leo. Suspendisse tellus purus, lobortis et eleifend eget, luctus gravida sem. Nam tempor et nunc scelerisque viverra. Sed et dignissim lorem. Maecenas eu nisl massa. Curabitur nisi ipsum, posuere et ante quis, ultrices malesuada mi. Integer euismod gravida risus. Suspendisse potenti. Ut a iaculis mauris, et tempor nisl. Aliquam vitae purus quis neque maximus viverra."]

def section(request, sectionNumber):
    if 1<= sectionNumber <= 3:
        return HttpResponse(sectionContent[sectionNumber - 1])
    else :
        return Http404("Section Not Found")