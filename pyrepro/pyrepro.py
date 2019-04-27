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
        self.dirty_suffix = '-dirty'
        self.commitish = self.repo.describe(
            describe_strategy=2,
            dirty_suffix=self.dirty_suffix).replace('/', '-')
        if self.dirty_suffix in self.commitish and allow_dirty:
            logger.warn(
                'Repository has unstaged changes. Creating artifacts, but marking them dirty.'
            )
        elif self.dirty_suffix in self.commitish:
            raise OSError(
                'Refusing to create artifacts with a dirty repository. Current diff: %s',
                self.repo.diff())

    def __call__(self, f):
        def rewritten(*args, **kwargs):
            output = kwargs.get(self.keyword) or ''
            parts = os.path.split(output)
            fname, ext = parts[-1].split(os.path.extsep)
            with_info = fname + '-' + self.commitish + '-' + str(
                self.hashed_config)[:10] + os.path.extsep + ext
            kwargs[self.keyword] = os.path.join(
                *(list(parts)[:-1] + [with_info]))
            return f(*args, **kwargs)

        return rewritten
