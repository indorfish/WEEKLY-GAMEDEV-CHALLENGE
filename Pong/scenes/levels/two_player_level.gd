extends Node2D

enum states {p1_serving, p2_serving, rally, gameover}
var current_state
@onready var player_1 = $paddle
@onready var player_2 = $paddle2
@onready var debug_shi = $debug_shi
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	current_state = states.p1_serving

func change_state(new_state):
	current_state = new_state
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	#debug text stuff	
	#debug_shi.set_text(str("Is_serving: ",player_1.is_serving))
	debug_shi.set_text(str("Current_state: ", current_state))
	#Sort state machine
	if current_state == states.p1_serving:
		player_1.is_serving = true
	elif current_state == states.p2_serving:
		player_2.is_serving = true
	elif current_state == states.rally:
		player_1.is_serving = false
		player_2.is_serving = false
	elif current_state == states.gameover:
		player_1.process_mode = Node.PROCESS_MODE_DISABLED
		player_2.process_mode = Node.PROCESS_MODE_DISABLED


func _on_p_1_collider_body_entered(body: Node2D) -> void:
	if body.is_in_group("ball"):
		player_2.points += 1
		print("P1: ",player_1.points)
		$Ball.queue_free()
		change_state(states.p2_serving)

func _on_p_2_collider_body_entered(body: Node2D) -> void:
	if body.is_in_group("ball"):
		player_1.points += 1
		print("P2: ",player_2.points)
		$Ball.queue_free()
		change_state(states.p1_serving)
