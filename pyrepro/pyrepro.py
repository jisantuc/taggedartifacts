import logging
import os
from pygit2 import (Repository, discover_repository)

logger = logging.getLogger(__name__)


class Artifact(object):
    def __init__(self, keyword, config={}, allow_dirty=False):
        self.keyword = keyword
        self.hashed_config = hash(''.join(
            ['{}{}'.format(k, v) for k, v in config.items()]))
        self.allow_dirty = allow_dirty
        self.repo = Repository(discover_repository(os.getcwd()))
        self.commitish = self.repo.describe(dirty_suffix='-dirty')
        if '-dirty' in commitish and allow_dirty:
            logger.warn(
                'Repository has unstaged changes. Creating artifacts, but marking them dirty.'
            )
        elif '-dirty' in commitish:
            raise OSError(
                'Refusing to create artifacts with a dirty repository. Current diff: %s',
                self.repo.diff())

    def __call__(self, f, *pos, **kw):
        def rewritten(*args, **kwargs):
            output = kwargs.get(keyword) or ''
            parts = list(os.path.split(output))
            fname, ext = parts[-1].split(os.path.extsep)
            with_info = fname + '-' + commitish + '-' + str(
                hashed_config)[:10] + ext
            kwargs[keyword] = os.path.join(*(parts[:-1] + [with_info]))
            return f(*args, **kwargs)

        return rewritten
