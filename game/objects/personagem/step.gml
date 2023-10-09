var _c = keyboard_check(vk_up);
var _b = keyboard_check(vk_down);
var _d = keyboard_check(vk_right);
var _e = keyboard_check(vk_left);

velh = (_d - _e) * vel;
velv = (_b - _c) * vel;

x += velh;
y += velv;

if(velh != 0 or velv != 0){
	movendo = 1;
}
else{
	movendo = 0;
}

if(_d) lado = 3
if(_e) lado = 2
if(_b) lado = 0
if(_c) lado = 1

sprite_index = sprites[movendo][lado];
