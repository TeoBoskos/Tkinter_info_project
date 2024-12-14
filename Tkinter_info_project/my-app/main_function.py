question_index = 0 # In order to track the current question.

# Function to handle user input.
def next_question(input_entry_str, user_info, questions, input_label, output_label, input_entry, next_button) -> None:
  """
  This function handles the user input and displays the user output.
  It checks the `question_index` and assigns each input to the answer.
  Then it proceeds to check if there are any more questions. If not, it
  generates the final message and displays it on output_label.

  Parameters: None

  Returns: None
  """

  global question_index

  # Save the current input.
  answer = input_entry_str.get().strip()
  if question_index == 0:
    user_info["name"] = answer
  elif question_index == 1:
    user_info["age"] = answer
  elif question_index == 2:
    user_info["gender"] = answer
  elif question_index == 3:
    user_info["hobby"] = answer

  input_entry_str.set("") # This clears the entry.

  # Move to the next question or display output.
  question_index += 1
  if question_index < len(questions):
    input_label.config(text=questions[question_index])
  else:
    final_message = (
      f"Hello {user_info['name']}! I know you are a {user_info['age']} year old "
      f"{user_info['gender']} and you like {user_info['hobby']}."
    )
    input_label.config(text="Thank you!")
    output_label.config(text=final_message)

    # Hide the entry and the button
    input_entry.pack_forget()
    next_button.pack_forget()
    print(final_message)
