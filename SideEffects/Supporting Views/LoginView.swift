//
//  LoginView.swift
//  SideEffects
//
//  Created by Kevin Tran on 10/28/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct LoginView: View {
    @State var selection: Int? = nil
    @EnvironmentObject var loginData: LoginData
    var body: some View {
        VStack {
            Text("Side Effects").font(Font.system(size: 60, design: .default))
            
            HStack {
                Text("Username")
                TextField("Username", text: $loginData.username, onEditingChanged: { isEditing in
                    }).foregroundColor(.primary).padding().textFieldStyle(RoundedBorderTextFieldStyle())

                Button(action: {
                    self.loginData.username = ""
                }) {
                    Image(systemName: "xmark.circle.fill").opacity(loginData.username == "" ? 0 : 1)
                }
            }.padding()
            
            HStack {
                Text("Password")
                TextField("Password", text: $loginData.password, onEditingChanged: { isEditing in
                    }).foregroundColor(.primary).padding().textFieldStyle(RoundedBorderTextFieldStyle())

                Button(action: {
                    self.loginData.password = ""
                }) {
                    Image(systemName: "xmark.circle.fill").opacity(loginData.password == "" ? 0 : 1)
                }
            }.padding()
            
            
            NavigationLink(destination: ThreadList(), tag: 1, selection: $selection) {
                Button(action: {
                    self.selection = 1
                    // self.loginData.password
                    // self.loginData.username
                }) {
                    Text("Submit")
                        .padding()
                        .foregroundColor(.white)
                        .background(LinearGradient(gradient: Gradient(colors: [Color.red,  Color.purple]), startPoint: .leading, endPoint: .trailing))
                        .cornerRadius(40)
                }
            }
            /*
            NavigationLink(destination: ThreadList()) {
                print(self.loginData.password)
                HStack {
                    Text("Submit")
                        .fontWeight(.semibold)
                }
                .padding()
                .foregroundColor(.white)
                .background(LinearGradient(gradient: Gradient(colors: [Color.green, Color.blue]), startPoint: .leading, endPoint: .trailing))
                .cornerRadius(40)
            }.padding().offset(y: 50)
            */
        }
    }
}

struct LoginView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
    }
}
