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
        self.errors=[]
        self.regexes = {'generic' : r'((?:Variable|Unsupported|Missing|Type).*)(.*\s)+(?:(?:at .*\:(\d+)))', 'multiple' : r'(.*?)s:'}
        super().__init__(lint)
    

    def find_errors(self, output):
        body = '\n'.join(output.split('\n')[1:])
        match = re.match(self.regexes['multiple'], body)

        if match:
            regex = r'line (\d+)';
            for line in re.findall(regex, body):
                yield True, int(line), 0, '','', match.group(1),''
        else:
            for result in re.findall(self.regexes['generic'], body):
                yield True, int(result[-1]), 0, '', '', result[0] if len(result) == 2 else ' '.join(result[:-1]), ''

    def cmd(self):
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
