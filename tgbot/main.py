import asyncio
import os

if os.getenv("USE_WEBHOOK") == "true":
    from webhook import run_webhooks

    main = run_webhooks
else:
    from polling import run_polling

    main = run_polling


if __name__ == "__main__":
    from .logger import *

    asyncio.run(main())
