import pytest
from playwright.sync_api import Playwright
from testla_screenplay import Actor

from src.testla_screenplay_playwright.api.abilities.use_api import UseAPI
from src.testla_screenplay_playwright.api.actions.delete import Delete
from src.testla_screenplay_playwright.api.actions.get import Get
from src.testla_screenplay_playwright.api.actions.head import Head
from src.testla_screenplay_playwright.api.actions.patch import Patch
from src.testla_screenplay_playwright.api.actions.post import Post
from src.testla_screenplay_playwright.api.actions.put import Put
from src.testla_screenplay_playwright.api.types import Response, ResponseBodyFormat


# execute tests with: pytest <file> --headed
# <file> not needed. if there os no <file>, all test files will be executed.
# -s if you need stdout output (print) 
# -k "test case" for only 1 specific test case

class TestAPI:
    actor: Actor

    @pytest.fixture(scope="function", autouse=True)
    def setup_request_context(self, playwright: Playwright):
        request_context = playwright.request.new_context()
        self.actor = Actor.named("Test Actor").can(UseAPI.using(request_context=request_context))

    def test_get(self):
        response: Response  = self.actor.attempts_to(
            Get.From('http://zippopotam.us/us/90210').with_response_body_format(ResponseBodyFormat.TEXT),
        )

        assert response.status == 200
        assert response.body is not None

    def test_post(self):
        data = { "title": 'foo', "body": 'bar', "userId": 1 }

        expected = { "title": 'foo', "body": 'bar', "userId": 1, "id": 101 }

        response: Response = self.actor.attempts_to(
            Post.To('https://jsonplaceholder.typicode.com/posts').with_data(data),
        )

        assert response.status == 201
        assert response.body == expected

    def test_put(self):
        data = { "id": 1, "title": 'foo', "body": 'bar', "userId": 1 }

        response: Response = self.actor.attempts_to(
            Put.To('https://jsonplaceholder.typicode.com/posts/1').with_data(data),
        )
        assert response.status == 200
        assert response.body == data

        response_with_headers: Response = self.actor.attempts_to(
            Put.To('https://jsonplaceholder.typicode.com/posts/1').with_data(data)
                .with_headers({
                    'Content-type': 'text/plain; charset=UTF-8',
                }),
        )
        assert response_with_headers.status == 200
        assert response_with_headers.body == { "id": 1 }

    def test_patch(self):
        data = { "userId": 1, "id": 1, "title": 'I patched this title!', "body": 'I patched this body!' }

        response: Response = self.actor.attempts_to(
            Patch.To('https://jsonplaceholder.typicode.com/posts/1').with_data(data),
        )
        assert response.status == 200
        assert response.body == data

        response_with_headers: Response = self.actor.attempts_to(
            Patch.To('https://jsonplaceholder.typicode.com/posts/1').with_data(data)
                .with_headers({
                    'Content-type': 'text/plain; charset=UTF-8',
                }),
        )
        assert response_with_headers.status == 200
        assert response_with_headers.body == {
            "userId": 1,
            "id": 1,
            "title": 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
            "body": 'quia et suscipit\n'
                + 'suscipit recusandae consequuntur expedita et cum\n'
                + 'reprehenderit molestiae ut ut quas totam\n'
                + 'nostrum rerum est autem sunt rem eveniet architecto',
        }

    def test_delete(self):
        response: Response = self.actor.attempts_to(
            Delete.From('https://jsonplaceholder.typicode.com/posts/1'),
        )
        assert response.status == 200
        assert response.body == {}

        response_with_headers: Response = self.actor.attempts_to(
            Delete.From('https://jsonplaceholder.typicode.com/posts/1')
                .with_headers({
                    'Content-type': 'text/plain; charset=UTF-8',
                }),
        )
        assert response_with_headers.status == 200
        assert response_with_headers.body == {} 

    def test_head(self):
        response: Response  = self.actor.attempts_to(
            Head.From('https://jsonplaceholder.typicode.com/posts/1'),
        )

        assert response.status == 200
        assert response.body is None