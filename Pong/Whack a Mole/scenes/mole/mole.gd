extends Area2D
enum states {DOWN, UP}#These are the states the the mole can be in
var current_state = states.DOWN#I set it to down.
@export var can_be_hit = false#This is to check if it can be hit by the mouse
var time: float#The time for the wait function (should be changed for the better)
@onready var color_modulator = $"color modulator"#The color modulator node
@onready var animator = $AnimationPlayer#The animator node
@onready var wait_timer = $"wait timer"
var timer_started = false
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	$"wait timer".start() # What happens when it starts/ enters scene tree

func change_state(new_state):#For changing the mole's state
	current_state = new_state
	
func wait(period, delta):#this is for creating timed delays(can be use once though
	time += delta
	#print(time)
	if int(time) == period:
		time = 0
		return true

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	
	if current_state == states.DOWN:#The DOWN state goes to the up state after some delay
		
		if !timer_started:# Code to make the timer called only once per refresh
			wait_timer.start()
			timer_started = true
		
	if current_state == states.UP:#The UP state goes to the down state when done
		animator.play("down")
	
	if Input.is_action_just_pressed("hit") and can_be_hit:#Play hit animation when hit (In progress)
		color_modulator.play("hit")
		animator.play("down")
	
	
#Do and undo the can_be_hit bool
################################
func _on_mouse_entered() -> void:
	can_be_hit = true


func _on_mouse_exited() -> void:
	can_be_hit = false
#################################

func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	if anim_name == "up":#Change state to up after up animation is done
		change_state(states.UP)
	
	if anim_name == "down":#Change state to down when down animation is done
		change_state(states.DOWN)


func _on_wait_timer_timeout() -> void:
	var rand_number = randi_range(1,2)#determine if per wait time the mole should rise.
	if rand_number == 1:
		animator.play("up")
