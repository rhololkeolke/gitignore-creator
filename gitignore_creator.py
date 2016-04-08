import click
import requests
import pyfiglet
import logging

GITIGNORE_REPO_URL = 'https://raw.githubusercontent.com/github/gitignore/master/'
GITIGNORE_REPO_GLOBAL_URL = 'https://raw.githubusercontent.com/github/gitignore/master/Global/'

@click.command()
@click.option('--output', type=click.STRING, default=".gitignore")
@click.argument('template_names', nargs=-1)
def gitignore_creator(output, template_names):

    fig = pyfiglet.Figlet()
    logger = logging.getLogger('gitignore_creator')
    
    output_buffer = []
    for template_name in template_names:
        logger.debug(template_name)

        output_buffer.append(fig.renderText(template_name))
        
        response = requests.get('{}{}.gitignore'.format(GITIGNORE_REPO_URL, template_name))
        if response.status_code != 200:
            response = requests.get('{}{}.gitignore'.format(GITIGNORE_REPO_GLOBAL_URL, template_name))
            if response.status_code != 200:
                logger.error('Could not find {} template in gitignore repo'.format(template_name))
                output_buffer.append('# Failed to find {} in gitignore repo'.format(template_name))
                continue

        output_buffer.append(response.text)

    output_string = '\n'.join(output_buffer)
    logger.debug(output_string)
        
    with click.open_file(output, 'w') as output_file:
        output_file.write(output_string)

if __name__ == '__main__':
    gitignore_creator()
