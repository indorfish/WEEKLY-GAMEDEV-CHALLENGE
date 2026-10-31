extends CharacterBody2D

@export var speed = 150.0
@export var acceleration = Vector2(1.09, 1.09)
@onready var ping_sfx = $Ping
@onready var pong_sfx = $Pong
@onready var out_of_bounds = $OutOfBounds
var possesion = "player_1"
func _ready():# Set initial ball velocity
	velocity = Vector2(speed, 1)
	

func _physics_process(delta):
#The physics for Le bouncing ball
	var collision = move_and_collide(velocity * delta)
	if collision:
		
		velocity = velocity.bounce(collision.get_normal())
		velocity.x *= acceleration.x
		velocity.y *= acceleration.y
		if possesion == "player_1":
			ping_sfx.play()
		if possesion == "player_2":
			pong_sfx.play()
		print(possesion)

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("player_1"):
		possesion = "player_1"
	elif body.is_in_group("player_2"):
		possesion = "player_2"
