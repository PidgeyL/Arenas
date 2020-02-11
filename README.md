# Arenas
Arg - Env - Ask  <br />
Library to try and get variables from the system environment, script
 arguments or interactively with the user  <br />
 <br />
**Note:** written for **python 3** <br />
**Note:** The code has been tested on **Ubuntu 16.04 LTS**

## How to use
If Arenas is available on a given system, you can import it as shown
 below:

    from areans import 
    arenas_get(some_env_var, some_arg, some_ask_text, required=True, non_interactive=False)

### Example uses:
    from areans import 
    arenas_get("my_api_key", ['-k', '--api-key'], 'Enter API key')
