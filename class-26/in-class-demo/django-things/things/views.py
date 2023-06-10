# What is going to be 'invoked' when a user visits your website?
from django.views.generic import TemplateView


# fancy way of using templates
class HomePageView(TemplateView):
    template_name = 'home.html'

    # emulate retrieving 'things' from a db
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # we assign a list to a key called "things" inside of context
        context["things"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/SoilRake.jpg",
                "title": "Rake",
                "description": "Better than a shovel or a broom for leaves. Like a pitch fork but less pokey.",
                "reference_url": "https://en.wikipedia.org/wiki/Rake_(tool)"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/92/Soup_Spoon.jpg",
                "title": "Spoon",
                "description": "An eating utensil. Better for soup and cereal than a fork.",
                "reference_url": "https://en.wikipedia.org/wiki/Spoon"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Spoon_Piknik_i_Parken_2017_%28175930%29.jpg/600px-Spoon_Piknik_i_Parken_2017_%28175930%29.jpg",
                "title": "Spoon",
                "description": "Spoon is also an American rock band from Austin, Texas.",
                "reference_url": "https://en.wikipedia.org/wiki/Spoon_(band)"
            },
        ]

        return context

