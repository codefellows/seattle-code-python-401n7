from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Thing


class ThingFrontTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.thing = Thing.objects.create(
            name="pickle", rating=1, reviewer=self.user, description="pickle description"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.thing), "pickle")

    def test_thing_content(self):
        self.assertEqual(f"{self.thing.name}", "pickle")
        self.assertEqual(f"{self.thing.reviewer}", "tester")
        self.assertEqual(self.thing.rating, 1)

    def test_list_page_status_code(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('thing_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('thing_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'things/thing_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('thing_list')
        response = self.client.get(url)
        things = response.context['object_list']
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0].name, "pickle")
        self.assertEqual(things[0].rating, 1)
        self.assertEqual(things[0].reviewer.username, "tester")

    def test_detail_page_status_code(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('thing_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('thing_detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'things/thing_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('thing_detail', args=(1,))
        response = self.client.get(url)
        thing = response.context['thing']
        self.assertEqual(thing.name, "pickle")
        self.assertEqual(thing.rating, 1)
        self.assertEqual(thing.reviewer.username, "tester")


class ThingApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = Thing.objects.create(
            name="rake",
            reviewer=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_thing.save()

    def test_things_model(self):
        thing = Thing.objects.get(id=1)
        actual_reviewer = str(thing.reviewer)
        actual_name = str(thing.name)
        actual_description = str(thing.description)
        self.assertEqual(actual_reviewer, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_thing_list(self):
        self.client.login(username="testuser1", password="pass")  # need to log in
        url = reverse("thing_list")
        response = self.client.get(url)
        # print("response context is:", response.context)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.context["things"]
        self.assertEqual(len(things), 1)
        # self.assertEqual(things[0]["name"], "rake")

    # def test_get_thing_by_id(self):
    #     url = reverse("thing_detail", args=(1,))
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     thing = response.data
    #     self.assertEqual(thing["name"], "rake")
    #
    # def test_create_thing(self):
    #     url = reverse("thing_list")
    #     data = {"reviewer": 1, "name": "spoon",
    #             "description": "good for cereal and soup"}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     things = Thing.objects.all()
    #     self.assertEqual(len(things), 2)
    #     self.assertEqual(Thing.objects.get(id=2).name, "spoon")
    #
    # def test_update_thing(self):
    #     url = reverse("thing_detail", args=(1,))
    #     data = {
    #         "reviewer": 1,
    #         "name": "rake",
    #         "description": "pole with a crossbar toothed like a comb.",
    #     }
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     thing = Thing.objects.get(id=1)
    #     self.assertEqual(thing.name, data["name"])
    #     self.assertEqual(thing.reviewer.id, data["reviewer"])
    #     self.assertEqual(thing.description, data["description"])
    #
    # def test_delete_thing(self):
    #     url = reverse("thing_detail", args=(1,))
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     things = Thing.objects.all()
    #     self.assertEqual(len(things), 0)
