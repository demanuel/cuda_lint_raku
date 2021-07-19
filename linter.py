import re
from cuda_lint import Linter, util

class RakuLint(Linter):
    """Provides an interface to raku -c"""

    cmd = None
    executable = 'raku'
    multiline = True
    syntax = ('Raku')
    base_cmd = ('-c')
    tempfile_suffix = '.raku'

    def __init__(self, lint):
        self.reason_regexes = [re.compile(r'(.*):', re.DOTALL|re.MULTILINE), re.compile(r'(.*)\vat',re.DOTALL|re.MULTILINE)]
        self.plural_regex   = re.compile(r'(.*)s:')
        self.line_regexes   = [re.compile(r':(\d+)'), re.compile('\s(\d+),?')]

        super().__init__(lint)

    def cmd(self):
        """Return the command line to execute."""

        result = self.executable + ' ' + self.base_cmd

        return result

    def find_errors(self, output):
        body = '\n'.join(output.split('\n')[1:])
        print(body)

        for reason in self.reason_regexes:
            m = reason.match(body)
            if m:
                reason = m.group(1)
                body = body.replace(reason, '') # remove the reason
                plural = self.plural_regex.match(reason)

                if plural:
                    reason = plural.group(1)

                for lrg in self.line_regexes:
                    lines = lrg.findall(body)
                    for line in lines:
                        yield True, int(line), 0, '', '', reason,''
