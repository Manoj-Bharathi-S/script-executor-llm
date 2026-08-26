import tools.set_alarm as sa
import tools.get_weather as gw
import tools.get_time as gt
import tools.screenshot as sc

def dispatch(name, args):
    """
    Routes a tool call from the model to the correct Python script.
    Returns a tuple: (action_description, execution_result)
    """
    try:
        if name == "set_alarm":
            action = f"Setting alarm for {args.get('hour')}:{args.get('minute'):02d} ({args.get('label', 'no label')})"
            result = sa.set_alarm(args.get('hour', 0), args.get('minute', 0), args.get('label', 'no label'))
            return action, result
            
        elif name == "get_weather":
            action = f"Fetching weather for {args.get('city')} in {args.get('units')}"
            result = gw.get_weather(args.get('city', ''), args.get('units', 'celsius'))
            return action, result
            
        elif name == "get_sys_time":
            action = "Fetching system time..."
            result = gt.get_system_time(args.get('format_12hr', False))
            return action, result
            
        elif name == "take_screenshot":
            action = f"Taking a screenshot..."
            result = sc.take_screenshot(args.get('filename'))
            return action, result
            
        else:
            return f"Unknown tool '{name}'", f"Error: No handler implemented for {name}."
            
    except Exception as e:
        return f"Executing {name}...", f"Error during execution: {str(e)}"
