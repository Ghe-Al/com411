import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.ascii_art as ascii_art
import basics.output.escape_characters as escape_characters
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input
import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function
import basics.modules.guess_the_number as guess_the_number
import basics.decisions.and_operator as and_operator
import basics.decisions.or_operator as or_operator
import basics.decisions.review as review
import basics.decisions.simple_decision.comparison_operators as comparison_operators
import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.ifi as ifi
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.decisions.nested_decisions.nested as nested
import basics.decisions.nested_decisions.nestception as nestception
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.range as ranger
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.simple as simple
import basics.repetitions.while_loop.ascii as ascii
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.while_loop.len as len
import basics.repetitions.while_loop.simple as simpler
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers
import basics.repetitions.nested_loop.nested as nesteds
import basics.repetitions.nested_loop.nesting as nesting

def run_block_a():
  print("Which program in 'Block A: Basics' do you wish to run?")
  response = input()
  if (response == "simple_message"):
    simple_message.run()
  if (response == "multiline_message"):
    multiline_message.run()
  if (response =="ascii_art"):
    ascii_art.run()
  if (response =="escape_characters"):
    escape_characters.run()
  if (response =="ascii_robot"):
    ascii_robot.run()
  if (response =="data_types"):
    data_types.run()
  if (response =="string_operators"):
    string_operators.run()
  if (response =="user_input"):
    user_input.run()
  if (response =="ascii_character"):
    ascii_character.run()
  if (response =="ascii_code"):
    ascii_code.run()
  if (response =="function_calls"):
    function_calls.run()
  if (response =="function_with_loop"):
    function_with_loop.run()
  if (response =="function_with_nesting"):
    function_with_nesting.run()
  if (response =="function_with_parameter"):
    function_with_parameter.run()
  if (response =="function_with_parameters"):
    function_with_parameters.run()
  if (response =="multiple_functions"):
    multiple_functions.run()
  if (response =="return_values"):
    return_values.run()
  if (response =="simple_function"):
    simple_function.run()
  if (response =="guess_the_number"):
    guess_the_number.run()
  if (response =="and_operator"):
    and_operator.run()
  if (response =="or_operator"):
    or_operator.run()
  if (response =="review"):
    review.run()
  if (response =="comparison_operators"):
    comparison_operators.run()
  if (response =="counter"):
    counter.run()
  if (response =="if_elif_else"):
    if_elif_else.run()
  if (response =="if_else"):
    if_else.run()
  if (response =="ifi"):
    ifi.run()
  if (response =="modulo_operator"):
    modulo_operator.run()
  if (response =="nested"):
    nested.run()
  if (response =="nestception"):
    nestception.run()
  if (response =="characters"):
    characters.run()
  if (response =="count_down"):
    count_down.run()
  if (response =="membership_operators"):
    membership_operators.run()
  if (response =="ranger"):
    ranger.run()
  if (response =="reverse"):
    reverse.run()
  if (response =="simple"):
    simple.run()
  if (response =="ascii"):
    ascii.run()
  if (response =="count"):
    count.run()
  if (response =="factorial"):
    factorial.run()
  if (response =="len"):
    len.run()
  if (response =="simpler"):
    simpler.run()
  if (response =="sum_100"):
    sum_100.run()
  if (response =="sum_user_numbers"):
    sum_user_numbers.run()
  if (response =="nesteds"):
    nesteds.run()
  if (response =="nesting"):
    nesting.run()

def run():
  is_running = True
  while(is_running):
    print("What would you like to do?")
    print("[a] Run 'Block A: Basics' programs")
    print("[q] Quit")
    response = input()
    if (response == "a"):
      run_block_a()
    elif (response == "q"):
      break
    else:
      print("Invalid option! Please try again.")
  run()