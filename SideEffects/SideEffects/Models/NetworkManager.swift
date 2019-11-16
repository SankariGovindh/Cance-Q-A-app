//
//  NetworkManager.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import Combine
import Foundation


class NetworkManager: ObservableObject {
    var dict: [Int: String] = [1: "login",
                               2: "add_user",
                               3: "add_question",
                               4: "add_comment",
                               5: "get_recent_questions",
                               6: "delete_question",
                               7: "update_question",
                               8: "update_comment",
                               9: "delete_comment",
                               10: "get_user_info",
                               11: "get_question_history"]
    
    func post(code: Int, uploadData: String) -> Bool {
        let url = URL(string: "http://127.0.0.1:5000/" + dict[code]! + uploadData)!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print ("error: \(error)")
                return
            }
            guard let response = response as? HTTPURLResponse,
                (200...299).contains(response.statusCode) else {
                print ("server error")
                return
            }
            if let mimeType = response.mimeType,
                mimeType == "application/json",
                let data = data,
                let dataString = String(data: data, encoding: .utf8) {
                print ("got data: \(dataString)")
            }
        }.resume()
        return true
    }
}
