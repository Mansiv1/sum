class RuleBot:
  #potential negative response
  negative_response = ("no, nope, sorry")
  #exit conservation keyword
  exit_commands = (" Good bye,bye,quite")
  #random starter questions
  random_questions = ("why are you here?, what planet have you visited?, what technology do you have on this planet ")
  
  def __init__(self):
    self.alienbabble = { 'describe the planet intent ':r'.*\s* your planet.*','answer_why_intent': r'why\sare.*'}

  def greet(self):
    self.name = input("what is your name?\n") 
    will_help = input(
        f"Hi {self.name}, I am Chat Bot. Will you help me learn about your planet ?\n")
    if will_help in self.negative_response:
        print("ok, have a Nice Day!")
        return
    self.chat()

  def make_exit(self, reply):
     for command in self.exit_commands:
       if reply == command:
          print("okay , have a nice earth day!")
          return True

  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
     reply = input(self.match_reply(reply))

  def match_reply(self, reply):
    for key, value in self.alienbabble.items():
       intent = key 
       regex_pattern = value
       found_match = re.match(regex_pattern, reply)
       if found_match and intent == 'describe_planet_intent':
         return self.describe_planet_intent()
       elif found_match and intent == 'answer_why_intent':
         return self.answer_why_intent()
       elif found_match and intent == 'about_intellipat':
          return self.about_intellipat()
    if not found_match:
      return self.no_match_intent()

  def describe_planet_intent(self):
      responses = ("my planet is a utopia ofdiverse")
      return random.choice(responses)

  def answer_why_intent(self):
     responses = (" i come in peace\n")
     return random.choice(responses)
  def about_intellipat(self):
   responses = ("intellipat is a wirld largest")
   return random.choice(responses)
  def no_match_intent(self):
    responses= ( "please tell me more")
    return random.choice(responses)

AlienBot = RuleBot()
AlienBot.greet() 
