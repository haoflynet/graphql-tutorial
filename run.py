import graphene

from db import DBSession
from schemas import get_dataloaders, Query
from mutations import Mutation

from sanic import Sanic
from sanic.testing import SanicTestClient
from sanic_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor

from web_template import TEMPLATE


def create_app(path="/graphql", **kwargs):
    app = Sanic(__name__)
    app.debug = True

    schema = graphene.Schema(query=Query, mutation=Mutation)

    @app.listener("before_server_start")
    def init_web_route(app, loop):
        print("初始化web路由")
        app.add_route(
            GraphQLView.as_view(
                schema=schema,
                context=dict({"session": DBSession()}, **get_dataloaders()),
                graphiql_template=TEMPLATE,
                **kwargs
            ),
            "/web",
        )

    @app.listener("before_server_start")
    def init_async_executor(app, loop):
        executor = AsyncioExecutor(loop)
        app.add_route(
            GraphQLView.as_view(
                schema=schema,
                executor=executor,
                context=dict({"session": DBSession()}, **get_dataloaders()),
                **kwargs
            ),
            path,
        )

    @app.listener("before_server_stop")
    def remove_graphql_endpoint(app, loop):
        app.remove_route(path)

    app.client = SanicTestClient(app)
    return app


if __name__ == "__main__":
    app = create_app(graphiql=True, async_executor=True)
    app.run(host="0.0.0.0", port=5000)
