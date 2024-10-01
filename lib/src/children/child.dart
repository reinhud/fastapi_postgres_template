class Child {
  String? id;
  String name = '';
  DateTime? birthdate;
  String? hobby;
  int? parentId;

  Child() {
    // Empty constructor for initialization
  }

  Child.fromJson(Map<String, dynamic> json) {
    name = json['name'];
    birthdate = json['birthdate'];
    hobby = json['hobby'];
    parentId = json['parent_id'];
  }

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'birthdate': birthdate,
      'hobby': hobby,
      'parent_id': parentId,
    };
  }
}