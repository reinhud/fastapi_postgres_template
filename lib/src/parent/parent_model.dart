import 'package:family/src/children/child.dart';

class Parent {
  String? id;
  String name = '';
  DateTime? birthdate;
  List<Child> children = [];

  Parent() {
    // Empty constructor for initialization
  }

  Parent.fromJson(Map<String, dynamic> json) {
    name = json['name'];
    birthdate = json['birthdate'];
  }

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'birthdate': birthdate,
    };
  }
}