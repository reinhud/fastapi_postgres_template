import 'package:dio/dio.dart';

const apiBaseURL = 'http://localhost:8000/api/';

class ApiService {
  String _url (String url) {
    return '$apiBaseURL$url';
  }

  Future<List<dynamic>> get(String url, [Map<String, dynamic> params = const {}]) async {
    final response = await Dio().get(_url(url), queryParameters: params);
    return response.data;
  }

  Future<dynamic> post(String url, [Map<String, dynamic> data = const {}]) async {
    final response = await Dio().post(_url(url), data: data);
    return response.data;
  }

  Future<dynamic> patch(String url, [Map<String, dynamic> data = const {}]) async {
    final response = await Dio().patch(_url(url), data: data);
    return response.data;
  }

  Future<dynamic> delete(String url) async {
    final response = await Dio().delete(_url(url));
    return response.data;
  }

}